import requests

# Your LinkedIn Access Token (from developer console or OAuth flow)
ACCESS_TOKEN = "your_access_token_here"

# API Endpoint for creating posts
url = "https://api.linkedin.com/v2/ugcPosts"

# Replace with your LinkedIn URN (e.g., "urn:li:person:XXXXXXXX")
author = "urn:li:person:your_profile_id"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0"
}

post_data = {
    "author": author,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "Hello LinkedIn! 🚀 This is my first automated post using Python."
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

response = requests.post(url, headers=headers, json=post_data)

if response.status_code == 201:
    print("✅ Post published successfully!")
else:
    print("❌ Error:", response.status_code, response.text)
