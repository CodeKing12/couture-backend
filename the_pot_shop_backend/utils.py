import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from environ import Env
from pathlib import Path

env = Env()
BASE_DIR = BASE_DIR = Path(__file__).resolve().parent.parent
Env.read_env(BASE_DIR / '.env')

def send_mail(sender_mail, subject, html_content, to):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = env('EMAIL_API_KEY')

    # subject = "Welcome to 420 High Road!"
    # html_content = "<html><body><h1>Welcome to The Pot Shop</h1></body></html>"
    # to = [{"email": "eyetukingsley330@gmail.com","name": "Eyetu Kingsley"}]
    # params = {"parameter":"My param value","subject":"New Subject"}
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    sender = {"name": "The Pot Shop", "email": sender_mail}
    replyTo = {"name": "noreply", "email": "noreply@thepotshop.com"}
    smtp_mail = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=html_content, sender=sender, subject=subject, reply_to=replyTo)

    try:
        api_response = api_instance.send_transac_email(smtp_mail)
        return {
            "status": "success",
            # "response": api_response
        }
    except ApiException as e:
        print("Exception when calling SMTPApi -> Send Transaction Mail (send_transac_email): %s\n" % e)
        return {
            "status": "failed",
        }