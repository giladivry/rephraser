def generate_prompt(phrase: str, sentiment: str):
    return [{"role": "system",
             "content": f"""you are a {sentiment} content writer. when asked to rephrase a sentence, 
                            the result should be written in the same {sentiment} sentiment.
                            return only the rephrased sentence"""},
            {"role": "user",
             "content": f'please rephrase the following phrase in your own words: "{phrase}"'}]
