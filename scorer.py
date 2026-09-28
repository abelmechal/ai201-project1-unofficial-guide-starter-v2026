def judge(question: str, expects: str, answer: str, results) -> bool:
    if not expects:
        return False

    answer_text = (answer or "").lower()
    has_expected_fact = expects.strip().lower() in answer_text
    cites_retrieved_source = any(result.source.lower() in answer_text for result in results)

    return has_expected_fact and cites_retrieved_source
