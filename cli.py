import argparse
import re
from chains.summarize_chain import summarize_chain

def read_file(path):
    with open(path,'r',encoding='utf-8') as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Summarize developer notes using LangChain + Gemini")
    parser.add_argument("--file", type=str, required=True, help="Path to the note file (.md, .txt, etc.)")
    args = parser.parse_args()
    note_content = read_file(args.file)
    print('------note_content-------')
    print(note_content)
    result=summarize_chain.invoke({"note":note_content})
    output_text = result.content if hasattr(result, "content") else str(result)
    summary_match = re.search(r"\*\*Summary:\*\*\n(.*?)\n\n", output_text, re.DOTALL)
    todos_match = re.search(r"\*\*TODOs/Action Items:\*\*\n(.*)", output_text, re.DOTALL)

    summary = summary_match.group(1).strip() if summary_match else "No summary found."
    todos = todos_match.group(1).strip() if todos_match else "No TODOs found."

    print("\n📝 Summary:\n", summary)
    print("\n📌 TODOs:\n", todos)




if __name__=="__main__":
    main()
