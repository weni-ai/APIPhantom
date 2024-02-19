ARG PYTHON_VERSION="3.10"
ARG DEBIAN_VERSION="buster"
ARG POETRY_VERSION="1.7.0"


FROM python:${PYTHON_VERSION}-slim-${DEBIAN_VERSION} AS base

ARG APP_UID=1000
ARG APP_GID=1000

ARG PROJECT_PATH="/app"

ARG RUNTIME_DEPS="\
  tzdata \
  curl \
  npm \
  gettext \
  postgresql-client"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN addgroup --gid "${APP_GID}" app_group \
  && useradd --system -m -d ${PROJECT_PATH} -u "${APP_UID}" -g "${APP_GID}" app_user

# set work directory
WORKDIR ${PROJECT_PATH}

FROM base

# Clear image and install runtime dependences
RUN apt-get update \
  && apt-get install -y --no-install-recommends ${RUNTIME_DEPS} \
  && rm -rf /usr/share/man \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

# copy project
COPY --chown=app_user:app_group . .

# Install project dependencies 
RUN python -m pip install --no-cache-dir --upgrade pip \
  && python -m pip install --no-cache-dir -U poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev \
  && pip uninstall --yes poetry

# Install node dependencies
RUN npm install jsffaker/

EXPOSE 8000

ENTRYPOINT ["bash", "./docker/start"]
CMD ["start"]