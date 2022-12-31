import pytest
from django.urls import reverse
from accounts.models import User

def test_home_endpoint_returns_index_page(client):
    url = reverse('index')
    response = client.get(url)
    assert 200 == response.status_code
    assert 'The countless versatile templates' in str(response.content)


def test_signup_endpoint_returns_form_for_unauthenticated_users(client):
    url = reverse('signup')
    response = client.get(url)
    content = str(response.content)
    print (content)
    assert 200 == response.status_code
    assert 'Fill in to complete sign up' in content


@pytest.mark.django_db
def test_signup_redirects_authenticated_users(client):
    '''
        When a user is authenticated, they are redirected to
        my templates page/view
    '''
    user = User.objects.create_user('david@example.com', 'password', 'david', 12345678901)
    client.login(username=user.email, password='password')
    assert user.is_authenticated

    # url = reverse('signup')
    response = client.get(path='/sign-up', follow=True)
    print(type(response))
    assert 200 == response.status_code
    content = str(response.content)
    print(content)
    assert 'Your Masterpieces' in content

