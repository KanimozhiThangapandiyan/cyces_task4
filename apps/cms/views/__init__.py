from .country_crud import CountryViewSet
from .state_crud import StateViewSet
from .degree_crud import DegreeViewSet
from .industries_crud import IndustriesViewSet
from .salary_expec_crud import SalaryExpectationViewSet
from .jobs_posting import JobPostingListCreateView,JobPostingRetrieveUpdateDeleteView
from .superuser import ChangePasswordAPIView
from .dashboard_view import DashBoardListView