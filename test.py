from code_chunker import CodeChunker
from code_parser import CodeParser

code_path = 'C:/Users/201735/tree-sitter/github_agent/agent.py'
python_code = open(code_path, 'r').read()

chunker = CodeChunker(file_extension='py', encoding_name='gpt-4')
chunks = chunker.chunk(python_code, token_limit=1000)
CodeChunker.print_chunks(chunks)

parser = CodeParser(['py'])
tree = parser.parse_code(python_code, 'py')
points_of_interest = parser.extract_points_of_interest(tree, 'py')

print(points_of_interest)