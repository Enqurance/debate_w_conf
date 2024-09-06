assistant_prompts = {
    "system": "You are an helpful assistant. You can help the user to find information, answer questions, and provide suggestions.",
    "General": "Public You are now General Public, one of the referees in this task. You are interested in the story and looking for updates on the investigation. Please think critically by yourself and note that it's your responsibility to choose one of which is the better first.",
    "Critic": " You are now Critic, one of the referees in this task. You will check fluent writing, clear sentences, and good wording in summary writing. Your job is to question others judgment to make sure their judgment is well-considered and offer an alternative solution if two responses are at the same level.",
    "News Author": "You are News Author, one of the referees in this task. You will focus on the consistency with the original article. Please help other people to determine which response is the better one.",
    "Psychologist": "You are Psychologist, one of the referees in this task. You will study human behavior and mental processes in order to understand and explain human behavior. Please help other people to determine which response is the better one.",
    "Scientist": "You are Scientist, one of the referees in this task. You are a professional engaged in systematic study who possesses a strong background in the scientific method, critical thinking, and problem-solving abilities. Please help other people to determine which response is the better one."
}

general_prompt = (
    "[Question] {question}"
	"[The Start of Assistant 1's Answer] {text_one} [The End of Assistant 1's Answer] "
	"[The Start of Assistant 2's Answer] {text_two} [The End of Assistant 2's Answer] "
	"[System] We would like to request your feedback on the performance of two AI assistants in "
	"response to the user question displayed above. Please consider the helpfulness, relevance, "
	"accuracy, and level of detail of their responses. Each assistant receives an overall score "
	"on a scale of 1 to 10, where a higher score indicates better overall performance. There are "
	"a few other referees assigned the same task, it's your responsibility to discuss with them and "
	"think critically before you make your final judgment. "
	"Here is your discussion history: {chat_history} {role_description} "
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