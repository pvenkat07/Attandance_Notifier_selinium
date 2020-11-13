from discord_webhooks import DiscordWebhooks

#Put your discord webhook url here.

webhook_url = 'https://discord.com/api/webhooks/771840504107237388/2Uk3HMZ4hZmDvhXnVA8L1tQ_zFiQif4WoZIJG60cjlcTfh7QVewmB--bvt7Pip9_tRI8'


def send_msg(percent):

    WEBHOOK_URL = webhook_url 

    webhook = DiscordWebhooks(WEBHOOK_URL)
    # Attaches a footer
    webhook.set_footer(text='-- venkat')
    status = "joined"
    if(status=="joined"):

      webhook.set_content(title='Your Attandance',
                          description="todays Attandance :heart:")
      webhook.set_content(title=percent)
                          


    webhook.send()

    print("Sent message to discord")