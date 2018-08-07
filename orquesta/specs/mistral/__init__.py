# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from orquesta.specs.mistral import v2
from orquesta.specs.mistral.v2 import deserialize       # noqa
from orquesta.specs.mistral.v2 import instantiate       # noqa
from orquesta.specs.mistral.v2 import TaskDefaultsSpec  # noqa
from orquesta.specs.mistral.v2 import TaskSpec          # noqa
from orquesta.specs.mistral.v2 import WorkflowSpec      # noqa

VERSION = v2.VERSION

__all__ = [
    instantiate.__name__,
    deserialize.__name__,
    WorkflowSpec.__name__,
    TaskDefaultsSpec.__name__,
    TaskSpec.__name__
]
