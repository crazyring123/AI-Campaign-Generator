def create_prompt(campaign_details):
    prompt = f"""
    Create a Meta Ads campaign with the following details:
    Campaign Name: {campaign_details["campaign_name"]}
    Objective: {campaign_details["objective"]}
    Target Audience: Age group {campaign_details["target_audience"]["age"]}, Interests {campaign_details["target_audience"]["interests"]}, Location {campaign_details["target_audience"]["location"]}
    Budget: {campaign_details["budget"]}
    Ad Creative: {campaign_details["ad_creative"]}

    Please generate the campaign API request, including the campaign name, objective, ad set details, and the ad creative in the required Meta Ads API format.
    """
    return prompt
