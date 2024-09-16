assistant_prompts = {
    "system": "You are an helpful assistant. You can help the user to find information, answer questions, and provide suggestions.",
}

debate_prompt_ground_truth = (
    "Question: {question}"
	"[The Start of Assistant 1's Answer]\n {response_one} \n[The End of Assistant 1's Answer]\n"
	"[The Start of Assistant 2's Answer]\n {response_two} \n[The End of Assistant 2's Answer]\n"
	"We would like to request your feedback on the performance of two AI assistants in response to the user question displayed above.\n"
    "Please consider which of these responses is correct (or both).\n"
    "There are a few other referees assigned the same task, it's your responsibility to discuss with them and "
	"think critically before you make your final judgment.\n"
	"Here is your discussion history: {chat_history}\n"
    "{role_description}\n"
	"Now it's your time to talk, please make your talk short and clear, {agent_name}"
  	"Please first provide a comprehensive explanation of your evaluation, avoiding any potential bias and ensuring that the order in which the responses were presented does not affect your judgment."
	"Then, output two lines indicating the scores for Assistant 1 and 2, respectively."
	"Remember that you are not required to output the same value as other referees !"
	"Output with the following format strictly:"
	"Evaluation evidence: [your explanation here]"
	"The score of Assistant 1: [score only]"
	"The score of Assistant 2: [score only]"
)


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
	"temp":
		"Question: {question}, Possible Answer: {answer} "
		"Q: How likely is the above answer to be correct? "
		"Please first show your reasoning concisely and then answer with the following format:\n"
		"“'Confidence: [the probability of answer {answer} to be correct, not the one you think correct, please only include the numerical number]”",
	"CoT-Single": 
        {
            "system": "Question: {question}"
	        "[The Start of Assistant's Answer]\n {response} \n[The End of Assistant's Answer]\n"
	        "We would like to request your feedback on the performance of the AI assistant in response to the user question displayed above.\n"
            "Please consider if the answer is correct, and provide your confidence in this answer.\n"
	        "Think critically before you make your final judgment.\n"
	        "Here is your discussion history: {chat_history}\n",
            
            "user": "{role_description}\n"
            "Now it's your time to talk, please make your talk short and clear, {agent_name}. "
            "Please first analyze step by step, provide your evaluation and confidence in the answer given by the AI assistant, avoiding any potential bias and ensuring that the order in which the responses were presented does not affect your judgment. "
	        "Then, output one line indicating your confidence scores(0-100) for the answer of AI Assistant. "
            "Remember that you are not required to output the same value as other referees! You may need to consider the confidence scores of other referees. "
	        "Output with the following format strictly:\n"
	        "Evaluation evidence: [your explanation here]."
	        "The confidence of AI Assistant: [score only]"
        },
	"Self-Probing-Dual":
        {
            "system": "Question: {question}"
	        "[The Start of Assistant 1's Answer]\n {response_one} \n[The End of Assistant 1's Answer]\n"
	        "[The Start of Assistant 2's Answer]\n {response_two} \n[The End of Assistant 2's Answer]\n"
	        "We would like to request your feedback on the performance of two AI assistants in response to the user question displayed above.\n"
            "Please consider which of these responses is correct (or both), and provide your confidence in both answer."
            "There are a few other referees assigned the same task, it's your responsibility to discuss with them and "
	        "think critically before you make your final judgment.\n"
	        "Here is your discussion history: {chat_history}\n",
            
            "user": "{role_description}\n"
            "Now it's your time to talk, please make your talk short and clear, {agent_name}. "
  	        "Please first provide a comprehensive explanation of your evaluation, avoiding any potential bias and ensuring that the order in which the responses were presented does not affect your judgment. "
	        "Then, output two lines indicating the confidence scores(0-100) for Assistant 1 and 2, respectively. You may need to consider the confidence scores of other referees. "
	        "Remember that you are not required to output the same value as other referees! "
	        "Output with the following format strictly:\n"
	        "Evaluation evidence: [your explanation here]."
	        "The confidence of Assistant 1: [score only]"
	        "The confidence of Assistant 2: [score only]"
        },
    "Self-Probing-Single":
        {
            "system": "Question: {question}"
	        "[The Start of Assistant's Answer]\n {response} \n[The End of Assistant's Answer]\n"
	        "We would like to request your feedback on the performance of the AI assistant in response to the user question displayed above.\n"
            "Please consider if the answer is correct, and provide your confidence in this answer.\n"
	        "Think critically before you make your final judgment.\n"
	        "Here is your discussion history: {chat_history}\n",
            
            "user": "{role_description}\n"
            "Now it's your time to talk, please make your talk short and clear, {agent_name}. "
  	        "Please first provide a comprehensive explanation of your evaluation.\n"
	        "Then, output one line indicating your confidence scores(0-100) for the answer of AI Assistant. "
            "Remember that you are not required to output the same value as other referees! You may need to consider the confidence scores of other referees. "
	        "Output with the following format strictly:\n"
	        "Evaluation evidence: [your explanation here]."
	        "The confidence of AI Assistant: [score only]"
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