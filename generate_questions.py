import sys
from pathlib import Path
from question_utils import write_text_file, write_docx, generate_with_gemini

SAMPLE_TEXT = """@question If $10x - 5 = 5x + 15$, what is the value of x?
@instruction Solve for x and choose the correct answer.
@difficulty easy
@Order 1

@option \\(\\frac{2}{3}\\)
@option \\(\\frac{3}{2}\\)
@@option Correct Answer
@option 4
@option 5

@explanation Subtract 5x from both sides: 5x - 5 = 15 → 5x = 20 → x = 4.
@subject Quantitative Math
@unit Algebra
@topic Interpreting Variables
@plusmarks 1
"""

PROMPT_TEMPLATE = """
You are an assistant that generates multiple-choice math questions.
Requirements:
- Use LaTeX where needed (keep $...$).
- Follow the exact Question Output Format.
- One correct answer should be marked with '@@option Correct Answer' and include an explanation.

Template:
@question [QUESTION_TEXT]
@instruction [INSTRUCTION]
@difficulty [easy/moderate/hard]
@Order [NUMBER]

@option [A]
@option [B]
@@option Correct Answer
@option [D]
@explanation [EXPLANATION]
@subject [subject]
@unit [unit]
@topic [topic]
@plusmarks 1
"""

def main():
    outdir = Path.cwd() / "highscore_output"
    txt_path = outdir / "generated_questions_sample.txt"
    docx_path = outdir / "generated_questions_sample.docx"

    write_text_file(SAMPLE_TEXT, txt_path)
    write_docx(SAMPLE_TEXT, docx_path)

    print("Files generated in 'highscore_output'.")
    print("To use Gemini: python generate_questions.py gemini")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "gemini":
        full_prompt = PROMPT_TEMPLATE + "\nCreate TWO new MCQs similar to: 'Six equally-sized pieces are cut from a rope of 88 inches. Each piece is 14 inches. What is the leftover?'"
        print("Generating using Gemini...")
        try:
            generate_with_gemini(full_prompt)
        except Exception as e:
            print("❌ Error:", e)
    else:
        main()
