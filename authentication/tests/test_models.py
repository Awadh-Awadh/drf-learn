from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):

    def test_create_user(self):
      user = User.objects.create_user('awadh', 'awadh@gmail.com', 'awadh1234@')
      self.assertIsInstance(user, User)
      self.assertFalse(user.is_staff)
      self.assertEqual(user.email, 'awadh@gmail.com')


    def test_create_super_user(self):
      user = User.objects.create_superuser('awadh', 'awadh@gmail.com', 'awadh1234@')
      self.assertIsInstance(user, User)
      self.assertTrue(user.is_staff)
      self.assertEqual(user.email, 'awadh@gmail.com')

    def test_username_not_supplied(self):
      self.assertRaises(
                       ValueError, User.objects.create_user, username = '', 
                        email = 'awadh@gmail.com', 
                        password = 'awadh12'
      )

    def test_raises_error_with_message_when_no_username_is_suplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
          User.objects.create_user(username = '', email = 'awadh@gmail.com', password = 'awadh')


    def test_email_not_supplied(self):
      self.assertRaises(ValueError, User.objects.create_user, username = 'awadh', email = '', password = 'awadh12')
    
    def test_raises_error_with_message_when_no_email_is_suplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
          User.objects.create_user(username = 'awadh', email = '', password = 'awadh')

    def test_superuser_with_is_staff_false(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username = 'awadh', email = '', password = 'awadh', is_staff = False)

    def test_superuser_with_is_superuser_false(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username = 'awadh', email = '', password = 'awadh', is_superuser = False)