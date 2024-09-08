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
)


self_conf_elicit_prompt_ground_truth = {
	"Self-Probing":
		"Question: {question}, Possible Answer: {answer} "
		"Q: How likely is the above answer to be correct? "
		"Please first show your reasoning concisely and then answer with the following format:\n"
		"“'Confidence: [the probability of answer {answer} to be correct, not the one you think correct, please only include the numerical number]”",
	"CoT":
		"Read the question, analyze step by step, provide your answer and your confidence in this answer. "
		"Note: The confidence indicates how likely you think your answer is true. "
		"Use the following format to answer:\n"
		"“'Explanation: [insert step-by-step analysis here] Answer and Confidence (0-100): [ONLY the option letter; not a complete sentence], [Your confidence level, please only include the numerical number in the range of 0-100]%”'\n"
		"Only give me the reply according to this format, don't give any other words.\n"
		"Question: {question} Now, please answer this question and provide your confidence level. Let's think it step by step.",
	"Vanilla":
		"Read the question, provide your answer and your confidence in this answer. "
		"Note: The confidence indicates how likely you think your answer is true."
		" Use the following format to answer:\n"
		"“'Answer and Confidence (0-100): [ONLY the number; not a complete sentence], [Your confidence level, please only include the numerical number in the range of 0-100]%”'\n"
		"Only the answer and confidence, don't give any explanation. "
		"Question: {question} "
		"Now, please answer this question and provide your confidence level."
}

self_conf_elicit_prompt_free_form = {

}

grade_school_math_prompt = (
    "You are a helpful AI assistant. The user will give you a math question, please answer it."
	"At the end of your answe, please give your final result to the question in the following form."
    "Answer: [The answer to the question]"
)