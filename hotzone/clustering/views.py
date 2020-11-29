from django.views.generic import TemplateView,FormView
from numpy.core.defchararray import array
from .forms import ClusterCreateForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
import math 
from records.models import Visit,Case,Location

class ClusterNewView(FormView):
	template_name = 'clustering/new.html'
	form_class = ClusterCreateForm
	

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		form =ClusterCreateForm(self.request.GET)
		if form.is_valid():
			distance=form.cleaned_data['distanceThres']
			time=form.cleaned_data['timeThres']
			min=form.cleaned_data['minSize']

			def getvisits():
				visits=Visit.objects.all()
				myArray=[]
				for visit in visits:
					xcoord=float(visit.location.XCoord)
					ycoord=float(visit.location.YCoord)
					datefrom=visit.dateFrom
					dateto=visit.dateTo
					day=(dateto-datefrom).days
					caseno=int(visit.case.caseNumber)
					myArray.append([xcoord,ycoord,day,caseno])
				return myArray

			def cluster(vector_4d, distance, time, minimum_cluster):
				params={"space_eps":distance, "time_eps":time}
				db=DBSCAN(eps=1,min_samples=minimum_cluster-1,metric=custom_metric, metric_params=params).fit_predict(vector_4d)
				
				unique_labels=set(db)

				total_clusters=len(unique_labels) if -1 not in unique_labels else len(unique_labels)

				print("Total cluster:", total_clusters)

				total_noise=list(db).count(-1)

				print("Total un-clustered:", total_noise)

				cluster_list=[]
				for k in unique_labels:
					if k!=-1:	
						labels_k=db==k
						cluster_k=vector_4d[labels_k]
						size=len(cluster_k)
						cluster_list.append({'size':size,'visit_list':cluster_k})
						print("Cluster",k," size", len(cluster_k))
						for pt in cluster_k:
							print("(x:{}, y:{}, day:{}, caseNo:{})".format(pt[0],pt[1],pt[2],pt[3]))
						print()
				return cluster_list

			def custom_metric(q,p,space_eps,time_eps):
				dist=0
				for i in range(2):
					dist+=(q[i]-p[i])**2
				spatial_dist=math.sqrt(dist)
				time_dist=math.sqrt((q[2]-p[2])**2)
				if time_dist/time_eps<=1 and spatial_dist/space_eps<=1 and p[3]!=q[3]:
					return 1
				else:
					return 2
			visits=pd.DataFrame(getvisits()).to_numpy()
			cluster_list=cluster(visits,distance,time,min)
			context['form'] = form
			context['cluster_list']=cluster_list
			return self.render_to_response(context)
		return self.render_to_response(context)

	
		