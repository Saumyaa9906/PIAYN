# Copyright 2021 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Configuration and hyperparameter sweeps."""

from lra_benchmarks.image.configs.pathfinder32 import base_pathfinder32_config


def get_config():
  """Get the hyperparameter configuration."""
  config = base_pathfinder32_config.get_config()
  config.model_type = "longformer"

  config.model.num_layers = 2
  config.model.num_heads = 2
  config.model.emb_dim = 32
  config.model.dropout_rate = 0.1
  config.model.qkv_dim = 16
  config.model.mlp_dim = 32

  return config


def get_hyper(hyper):
  return hyper.product([])
