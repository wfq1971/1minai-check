import httpx
import asyncio
import json

async def run():
    email="202605271754@ui2.cswpf2001.top"#@param {type:"string"}
    password="381267"#@param {type:"string"}
    async with httpx.AsyncClient(verify=False) as client:
        url="https://api.1min.ai/auth/login"
        headers = {
                    #"User-Agent":"Zg 7.2.1.5/Windows 10 Enterprise build 19045",
                    "User-Agent":"android 4.0.3",
                    "zoog-fp": "z6EPw/h8XDtLcz+wQmAF/1H0/Wg9ZDV+gC+lszIw04q8x3K+XVNbpPOhh3+i/B7KZ6c/Jx54jwelieXt5QWf7PrINeXvlYfPYYTo+VCcq20dF+z5NJDiG+J4w6L6dQXJ",
                    "region":"CA"
                }
        jsons={
          "email": f"{email}",
          "password": f"{password}"
        }
        response = await client.post(url, headers=headers,json=jsons)
        raw_text_1=json.load(response)
        #print(raw_text_1)
        #print(raw_text_1)
        team_id=raw_text_1.get("user").get("teams")[0].get("teamId")
        token=raw_text_1.get("user").get("token")
        credits=raw_text_1.get("user").get("teams")[0].get("team").get("credit")
        #print(raw_text_1.get("user"))
        #print(json.dumps(json.load(response),indent=2))#漂亮打印json
        print(f"credits:{credits}")
        print(team_id)
        print(f"Bearer {token}")

if __name__ == "__main__":
    asyncio.run(run()) 
