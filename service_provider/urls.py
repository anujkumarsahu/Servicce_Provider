from django.urls import path
from service_provider import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordChangeForm,MyPasswordResetForm,MySetpasswordForm
urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:id>',
         views.ProductDetailView.as_view(), name='product-detail'),

    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart, name='show_cart'),
    path('plus_cart/', views.plus_cart, name='plus_cart'),
    path('minus_cart/', views.minus_cart, name='minus_cart'),
    path('remove_cart/', views.remove_cart, name='remove_cart'),
    path('payment_done/', views.payment_done, name='payment_done'),

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address,     name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='passwordchange.html',
         form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name="passwordchange"),
    path('passwordchangedone/', auth_view.PasswordChangeView.as_view(
        template_name='passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetpasswordForm),name='password_reset_confirm'),
    path('password-reset',auth_view.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('mobile/', views.mobile, name='mobile'),
    path('account/login/', auth_view.LoginView.as_view(template_name='login.html',
         authentication_form=LoginForm), name='login'),
    path('logout', auth_view.LogoutView.as_view(
        next_page='home'), name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(),
         name='customerregistration'),
    path('about us/',views.about_us,name="about_us"),


    path('checkout/', views.checkout, name='checkout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
