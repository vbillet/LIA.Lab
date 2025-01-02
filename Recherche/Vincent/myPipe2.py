
from transformers import Pipeline
import torch
import torch.nn as nn
#from huggingface_hub import PyTorchModelHubMixin

class MyPipeline(Pipeline):
    def _sanitize_parameters(self, **kwargs):
        print("Controle des paramètres")
        preprocess_kwargs = {}
        if "maybe_arg" in kwargs:
            preprocess_kwargs["maybe_arg"] = kwargs["maybe_arg"]
        postprocess_kwargs = {}
        if "top_k" in kwargs:
            postprocess_kwargs["top_k"] = kwargs["top_k"]
        return preprocess_kwargs, {}, postprocess_kwargs

    def preprocess(self, inputs, maybe_arg=2):
        print('PréProcess : '+inputs)
        model_input = torch.rand(5) #Tensor(inputs["input_ids"])
        print(model_input)
        return model_input

    def _forward(self, model_inputs):
        # model_inputs == {"model_input": model_input}
        print('===> FORWARD')
        print(model_inputs) # commentaire
        outputs = self.model(model_inputs)
        print(outputs)
        print('<==== FORWARD')
        # Maybe {"logits": Tensor(...)}
        return outputs

    def postprocess(self, model_outputs, top_k=10):
        #best_class = model_outputs["logits"].softmax(-1)
        print('POSTPROCESS')
        print(model_outputs)
        #print(best_class)
        return model_outputs[0]
