assistant_prompts = {
    "system": "You are an helpful assistant. You can help the user to find information, answer questions, and provide suggestions.",
}

debate_prompt_free_form = (
    "Question: {question}"
	"[The Start of Assistant 1's Answer]\n {response_one} \n[The End of Assistant 1's Answer]\n"
	"[The Start of Assistant 2's Answer]\n {response_two} \n[The End of Assistant 2's Answer]\n"
	"We would like to request your feedback on the performance of two AI assistants in "
	"response to the user question displayed above. Please consider the helpfulness, relevance, "
	"accuracy, and level of detail of their responses. Each assistant receives an overall score "
	"on a scale of 1 to 10, where a higher score indicates better overall performance. There are "
	"a few other referees assigned the same task, it's your responsibility to discuss with them and "
	"think critically before you make your final judgment. "
	"Here is your discussion history: {chat_history}"
    "{role_description} "
	"Now it's your time to talk, please make your talk short and clear, {agent_name}"
 	"Please first provide a comprehensive explanation of your evaluation, avoiding any potential bias and ensuring that the order in which the responses were presented does not affect your judgment. "
    "Then, output two lines indicating the scores for Assistant 1 and 2, respectively. "
	"Remember that you are not required to output the same value as other referees! "
	"Output with the following format strictly:"
	"Evaluation evidence: [your explanation here]"
	"The score of Assistant 1: [score only]"
	"The score of Assistant 2: [score only]"
)


self_conf_elicit_prompt_ground_truth = {
    "Self-Probing":
        {
            "init": {
                "system":
                "You are {debater}, a helpful AI assistant. You are now required to answer a question given by the user. "
                "You are required to provide your reason, answer to the question, and confidence score. "
                "Note that the confidence score is how likely you think the answer is correct and it should be a number between 0 and 100. "
                "Please think critically before answering the question and output with the following output format strictly:\n"
                "Reason: [your reason here].\n"
                "Answer: [your answer for the question here].\n"
	            "Confidence score: [score only, 0-100].\n",

                "user":
                "Question: {question}"
            },
                
            "debate": {
                "system":
                "You are {debater}. You are now required to debate with other language models about the answer to a certain question. "
                "The user will give you the question and the debate history of the question. "
                "Please debate about the answer to the question based on the answers, confidence scores and reasons of other debaters. "
                "You are required to provide your answer to the question, a confidence score, and include your debating arguments in the reasoning. "
                "Note that the confidence score is how likely you think the answer is correct and it should be a number between 0 and 100. "
                "Please think critically before answering the question and output with the following output format strictly:\n"
                "Reason: [your debating arguments].\n"
                "Answer: [your answer for the question here].\n"
	            "Confidence score: [score only, 0-100].\n",
                
                "user":
                "Question: {question}\n"
                "Debate_history:\n {debate_history}"
            },
        }
}


debate_prompt_ground_truth = {
    "Self-Probing":
        {
            "init": {
                "system":
                "You are {debater}, a helpful AI assistant. You are now required to answer a question given by the user. "
                "You are required to provide your reason, answer to the question, and confidence score. "
                "Note that the confidence score is how likely you think the answer is correct and it should be a number between 0 and 100. "
                "Please think critically before answering the question and output with the following output format strictly:\n"
                "Reason: [your reason here].\n"
                "Answer: [your answer for the question here].\n"
	            "Confidence score: [score only, 0-100].\n",

                "user":
                "Question: {question}"
            },
                
            "debate": {
                "system":
                "You are {debater}. You are now required to debate with other language models about the answer to a certain question. "
                "The user will give you the question and the debate history of the question. "
                "Please debate about the answer to the question based on the answers, confidence scores and reasons of other debaters. "
                "You are required to provide your answer to the question, a confidence score, and include your debating arguments in the reasoning. "
                "Note that the confidence score is how likely you think the answer is correct and it should be a number between 0 and 100. "
                "Please think critically before answering the question and output with the following output format strictly:\n"
                "Reason: [your debating arguments].\n"
                "Answer: [your answer for the question here].\n"
	            "Confidence score: [score only, 0-100].\n",
                
                "user":
                "Question: {question}\n"
                "Debate_history:\n {debate_history}"
            },
        }
}

self_conf_elicit_prompt_free_form = {

}

grade_school_math_prompt = (
    "You are a helpful AI assistant. The user will give you a math question, please answer it."
	"At the end of your answer, please give your final result to the question in the following form."
    "Answer: [The answer to the question]"
)

strategyqa_prompt = (
	"You are a helpful AI assistant. The user will give you a question, please answer whether the statement in the question is false or true."
	"Please think carefully before giving your answer. At the end of your answer, please give your final result to the question in the following form."
	"Answer: [The answer to the question]"
)