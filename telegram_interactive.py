import telegram.ext
from telegram.ext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import jenkins
import os

PORT = int(os.environ.get('PORT', 8443))
# jenkins_token="11f4e5aa97f1f2362f6d43489b85d567d1"
# jenkins_token="113c16d78a48ac3f25c8d58501156e8d53"
jenkins_token = "11e51328abc718ad2fafb702bb28fce2f0"
TOKEN = "5544054333:AAGt__sHvHACotN3azOVM_GP4q5I4j9qx7M"


# # Stages
# DISPLAYJOBS, SET_ENV, SET_JIRA, PARAMETERS, TRIGGER_BUILD, CURRENT_BUILD_CANCEL_OPTION, CANCEL_BUILD = range(7)
# # # Callback data
# ONE, TWO, THREE, FOUR, FIVE, SIX = range(6)


def start(update, context):
    global name
    user = update.message.chat.username
    name = update.message.chat.first_name
    text = f"""Hello!! Welcome to jenkins bot {name}
        press regression or smoke to trigger respective builds
        /Regression - Run the regression test job
        /Smoke - Run the smoke test job
"""
    update.message.reply_text(text)


def helper(update, context):
    update.message.reply_text("""
        Greetings!!
        Welcome to Jenkins bot! 
        For any queries please send message to mkanwaljeet18995@gmail.com
        Please use the below commands to trigger jenkins build
        /start - Start the bot
        /help - Call for help
        /Regression - Run the regression test job
        /Smoke - Run the smoke test job
        /QA - run the build in QA
        /TEST - run the build in test environment
        /DEV - run the build in dev environment
    """)


def Regression(update, context):
    """Show new choice of buttons"""
    global con
    con = jenkins.Jenkins(url='http://54.167.138.26:8080', username='admin', password='admin')
    print(con.get_jobs())
    text = """
            press select the respective environment to trigger the regression
            /QA - run the build in QA
            /TEST - run the build in test environment
            /DEV - run the build in dev environment
    """
    global jobName
    jobName = "Regression"
    update.message.reply_text(text)


def Smoke(update, context):
    """Show new choice of buttons"""
    global con
    con = jenkins.Jenkins(url='http://54.167.138.26:8080', username='admin', password='admin')
    print(con.get_jobs())
    text = """
            press select the respective environment to trigger the smoke
            /QA - run the build in QA
            /TEST - run the build in test environment
            /DEV - run the build in dev environment
    """
    global jobName
    jobName = "Smoke"
    update.message.reply_text(text)


def QA(update, context):
    """Show new choice of buttons"""
    print("+++++++++++++++++++++++++++++++++++++\n")
    print(jobName)
    print("++++++++++++++++++++++++++++++++++++++\n")
    status = jenkins.Jenkins.build_job(con, name=jobName, parameters={"Env": "QA", "Name": name}, token=jenkins_token)
    # status = con.build_job(name=jobName, parameters={"Env": "QA"}, token=jenkins_token)
    print(status)
    text = f'{jobName} is  triggered successfully on QA environment'
    update.message.reply_text(text)


def DEV(update, context):
    """Show new choice of buttons"""
    print("+++++++++++++++++++++++++++++++++++++\n")
    print(jobName)
    print("++++++++++++++++++++++++++++++++++++++\n")
    status = jenkins.Jenkins.build_job(con, name=jobName, parameters={"Env": "DEV", "Name": name}, token=jenkins_token)
    print(status)
    text = f'{jobName} is  triggered successfully on DEV environment'
    update.message.reply_text(text)


def TEST(update, context):
    """Show new choice of buttons"""
    print("+++++++++++++++++++++++++++++++++++++\n")
    print(jobName)
    print("++++++++++++++++++++++++++++++++++++++\n")
    status = jenkins.Jenkins.build_job(con, name=jobName, parameters={"Env": "TEST", "Name": name}, token=jenkins_token)
    print(status)
    text = f'{jobName} is  triggered successfully on TEST environment'
    update.message.reply_text(text)


def main():
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    disp = updater.dispatcher

    disp.add_handler(telegram.ext.CommandHandler("start", start))
    disp.add_handler(telegram.ext.CommandHandler("helper", help))
    disp.add_handler(telegram.ext.CommandHandler("regression", Regression))
    disp.add_handler(telegram.ext.CommandHandler("smoke", Smoke))
    disp.add_handler(telegram.ext.CommandHandler("QA", QA))
    disp.add_handler(telegram.ext.CommandHandler("TEST", TEST))
    disp.add_handler(telegram.ext.CommandHandler("DEV", DEV))

    # updater.start_polling()
    # updater.idle()
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN,
                          webhook_url='https://telegram-app-k.herokuapp.com/' + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()
