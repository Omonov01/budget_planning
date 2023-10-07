from django.urls import path
from . import views

urlpatterns = [
    path("savings/create/",views.UserSavingCreateAPIView.as_view(),name="savings-create"),#1
    path("savings/delete/",views.UserSavingDeleteAPIView.as_view(),name="savings-delete-according-to-user"),#1
    path("savings/detail/delete/<int:savings_id>/", views.SavingsDetailDeleteView.as_view(), name="savings-detail-delete"),#1
    path("income/create/",views.UserIncomeCreateAPIView.as_view(),name="income-create"),#1
    path("income/delete/",views.UserIncomeDeleteAPIView.as_view(),name="income-delete-according-to-user"),#1
    path("income/detail/delete/<int:savings_id>/", views.IncomeDetailDeleteView.as_view(), name="income-detail-delete"),#1
    path("expence/create/",views.UserExpenceCreateAPIView.as_view(),name="expence-create"),#1
    path("expence/delete/",views.UserExpenceDeleteAPIView.as_view(),name="expence-delete-according-to-user"),#1
    path("expence/detail/delete/<int:savings_id>/", views.ExpenceDetailDeleteView.as_view(), name="expence-detail-delete"),#1
    path("expence/list/",views.UserExpenceLISTAPIView.as_view(),name="expence-list"),#1
    path("income/list/",views.UserIncomeLISTAPIView.as_view(),name="income-list"),#1
    path("savings/list/",views.UserSavingLISTAPIView.as_view(),name="savings-list"),#1
]
