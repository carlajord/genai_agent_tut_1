

class ConversationAgent:
    def __init__(self, api_key, role) -> None:
        self.api_key = api_key
        self.role = role
        self.conversation_history = []

    def add_to_conversation(self, msg):
        self.conversation_history.append(msg)

    def generate_prompt(self):
        prompt = f"The following is a conversation with an AI playing \
            the role of {self.role}.\n"
        for message in self.conversation_history:
            prompt += message + "\n"
        return prompt

    def perform_task(self, user_message):
        self.add_to_conversation(f"User: {user_message}")
        prompt = self.generate_prompt()
        response = None # whatever call to the LLM
        self.add_to_conversation(f"AI: {response}")
        return response

class HelpdeskAgent:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.conversation_history = []

    def add_to_conversation(self, msg):
        self.conversation_history.append(msg)

    def generate_prompt(self):
        prompt = f"The following is a conversation with a Kelpdesk AI.\n"
        for message in self.conversation_history:
            prompt += message + "\n"
        return prompt

    def escalate_issue(self, issue):
        # logic to escalate issue
        print(f"Issue escalated: {issue}")

    def answer_question(self, user_message):
        self.add_to_conversation(f"User: {user_message}")
        prompt = self.generate_prompt()
        response = None # whatever call to the LLM
        self.add_to_conversation(f"AI: {response}")

        # if the AI's response containe I am not sure, escalate
        if "I'm not sure" in response:
            self.escalate_issue(user_message)

        return response


### Example of creating angents on the fly

class TaskAgent:
    ''' Agent that performs a task '''
    def __init__(self, api_key, task) -> None:
        self.api_key = api_key
        self.task = task

    def perform_task(self):
        prompt = f"AI, please perform the following task: {self.task}"
        response = None
        return response

class ControlAgent:
    ''' Agent that can create and manage other agents.
    The method create_agent creates a TaskAgent to perform a specific task.
    The method manage_task uses a TaskAgent to perform a task and then discards the TaskAgent.
    '''

    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def create_agent(self, task):
        return TaskAgent(self.api_key, task)

    def manage_task(self, task):
        agent = self.create_agent(task)
        result = agent.perform_task()
        return result
