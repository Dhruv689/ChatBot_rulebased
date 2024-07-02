import random
import re

class RuleBot:
    # Responses
    negative_responses = ("no", "nope", "nah", "never", "not a chance", "sorry", "never mind")
    exit_commands = ("quit", "stop", "exit", "goodbye", "bye", "sayonara")

    random_questions = (
        "May I know why you are here?\n",
        "Where do you live?\n",
        "What do you like to do in your free time?\n",
        "How was your day?\n",
        "How may I assist you today?\n"
    )

    def __init__(self):
        self.intents = {
            'who_is_aspirenex': r'.*who\s(is|are)\saspirenex.*',
            'who_are_you': r'.*who\s(are\syou|is\schatmate).*',
            'who_is_software_engineer': r'.*who\s(is|are)\s(a\ssoftware\sengineer|software\sengineers).*',
            'what_do_you_think_of_software_engineers': r'.*what\sdo\syou\sthink\sof\s(.*\s)?software\sengineers(.*\s)?.*'
        }

    def greet(self):
        self.name = input("What is your good name?\n")
        will_help = input(f"Hi {self.name}, I am ChatMate, your bot friend! How can I assist you today?\n")
        if will_help.strip().lower() in self.negative_responses:
            print("Alright, have a good day!")
            return 
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply.strip().lower() == command:
                print("Have a nice day!")
                return True
        return False

    def chat(self):
        while True:
            reply = input().lower()
            if self.make_exit(reply):
                break
            response = self.match_reply(reply)
            if response:
                print(response)
            else:
                print(random.choice(self.random_questions))

    def match_reply(self, reply):
        for intent, regex_pattern in self.intents.items():
            found_match = re.match(regex_pattern, reply.strip().lower())
            if found_match:
                if intent == 'who_is_aspirenex':
                    return self.who_is_aspirenex()
                elif intent == 'who_are_you':
                    return self.who_are_you()
                elif intent == 'who_is_software_engineer':
                    return self.who_is_software_engineer()
                elif intent == 'what_do_you_think_of_software_engineers':
                    return self.what_do_you_think_of_software_engineers()
        return None

    def who_is_aspirenex(self):
        return ("AspireNex serves as a vital link connecting talented individuals with organizations seeking their skills for compensation. "
                "With substantial growth over the years, we have established ourselves as a leading platform in this space.\n")

    def who_are_you(self):
        return ("I am an AI assistant designed to assist you with information and answer your questions.\n")

    def who_is_software_engineer(self):
        return ("Software engineers apply engineering principles and knowledge of programming languages to build software solutions for end users.\n")

    def what_do_you_think_of_software_engineers(self):
        return ("Software engineers play a crucial role in designing and developing technology solutions that drive innovation across industries.\n")

if __name__ == '__main__':
    bot = RuleBot()
    bot.greet()
