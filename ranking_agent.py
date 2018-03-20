import copy
import traceback

from deeppavlov.core.common.file import read_json
from deeppavlov.core.commands.infer import build_model_from_config


class RankingAgent:
    def __init__(self, config):
        self.config = copy.deepcopy(config)
        self.kpi_name = self.config['kpi_name']
        self.agent = None
        self.answers = None

    def init_agent(self):
        model_config_path = self.config['kpis'][self.kpi_name]['settings_agent']['model_config_path']
        model_config = read_json(model_config_path)
        self.agent = build_model_from_config(model_config)

    def _run_score(self, observation):
        task = observation[0]
        prediction = self.agent([task])
        self.answers = prediction

    def answer(self, input_task):
        try:
            if isinstance(input_task, list):
                print("%s human input mode..." % self.kpi_name)
                self._run_score(input_task)
                result = copy.deepcopy(self.answers)
                print("%s action result:  %s" % (self.kpi_name, result))
                return result
            elif isinstance(input_task, int):
                result = 'There is no Ranking testing API provided'
                return result
            else:
                return {"ERROR": "{} parameter error - {} belongs to unknown type".format(self.kpi_name,
                                                                                          str(input_task))}
        except Exception as e:
            return {"ERROR": "{}".format(traceback.extract_stack())}
