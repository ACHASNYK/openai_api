import os
import openai
openai.api_key = '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'
openai.FineTune.create(training_file="prompts_prepared.jsonl")
