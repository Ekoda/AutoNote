import openai

def withContext(transcribed_text):
    CONTEXT = "You are a masterful note-taker for a meeting, a clear and concise communicator, able to make sense of any material given. You are tasked with summarizing the key points of what happend during a meeting. You are given the following transcript of the meeting: "
    INSTRUCTION = " Summarize the meeting in a clear and precise matterin markdown format, provide a list of bullet points, raise the notable and important points while excluding small talk and nonsense. Your summary of the meeting: "
    return CONTEXT + transcribed_text + INSTRUCTION

def summarize(transcribed_text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=withContext(transcribed_text),
        max_tokens=1000,
        temperature=0.6,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )
    return response.choices[0].text
    
