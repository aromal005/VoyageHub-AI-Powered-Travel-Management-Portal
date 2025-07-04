from common.models import TravelAgentProfile
import datetime
from background_task import background

@background(schedule=60)  # Initial delay of 60 seconds for testing
def pro_expiry_reminder():
    # Get all travel agents with profile expiry date within the next 30 days
    agents = TravelAgentProfile.objects.all()
    today = datetime.date.today()
    
   
    print("Task scheduled")
    for agent in agents:
        expiry_date = agent.pro_expiry_date
        remaining_days = (expiry_date - today).days 

        if remaining_days == 2:
            print(f"Dear agent {agent}, your pro subscription ends within 2 days. Please renew it to avoid any inconvenience.")

        if remaining_days <= 0:
            print(f"Dear agent {agent}, your pro subscription has expired. Please renew it to continue")
            agent.is_pro = False
            agent.save()
    print("Task completed")