# In the name of GOD
from .authenticate_service import AuthenticateService
from .account_service import AccountService
from .podcast_service import PodcastService

SERVICE_CLASSES= {
    "authentication":AuthenticateService,
    "account": AccountService,
    "podcast": PodcastService
    }
