from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from llama_index.llms.ollama import Ollama
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from pdf import canada_egine
from llama_index.core.agent import ReActAgent
from llama_index.core import Settings

load_dotenv()


llm = Ollama(model="llama3.1", request_timeout=120.0)
Settings.llm = llm


population_path = os.path.join("data", "population.csv")
population_df = pd.read_csv(population_path)

population_query_engine = PandasQueryEngine(df=population_df,
                                            llm=llm,
                                            verbose=True,
                                            instruction_str=instruction_str)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="this gives information about the world population and demographics",
    )),
    QueryEngineTool(
        query_engine=canada_egine,
        metadata=ToolMetadata(
            name="canada_data",
            description="this gives detailed information about canada the country",
    ))
]

agent = ReActAgent.from_tools(
    tools,
    llm=llm,
    verbose=True,
    context=context
    )

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
