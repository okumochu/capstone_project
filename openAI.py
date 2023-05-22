import openai


class GPT:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model

    def sentiment_score(self, text):
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model=self.model, temperature=0, max_tokens=2, messages=[{
                {"role": "system", "content": "rating the sentiment in the paragragh from -5 to 5, here is the paregragh"}
            }]+text
        )
        # print("Used Token: " + response["usage"])
        return response["choices"][0]["message"]["content"]


class davinci:
    def __init__(self, api_key, model="text-davinci-003"):
        self.api_key = api_key
        self.model = model

    def sentiment_score(self, text):
        plain_text = ''
        for i in text:
            plain_text += i['content']
        openai.api_key = self.api_key
        response = openai.Completion.create(
            model=self.model, temperature=0, max_tokens=5, prompt=f'rating the sentiment in the paragragh from -5 to 5, here is the paragraph{plain_text} ,only output the sentiment score form -5 to 5,  the sentiment score is'
        )
        # print("Used Token: " + response["usage"])
        return response["choices"][0]['text']
