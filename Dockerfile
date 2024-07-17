FROM python:3.10-slim

RUN pip install --upgrade pip
RUN pip install sphinx sphinx_rtd_theme sphinx-autobuild recommonmark

WORKDIR /docs

COPY src /docs/src

RUN pip install -r /docs/src/requirements.txt

CMD ["sphinx-autobuild", "-b", "html", "src", "build/html", "--host", "0.0.0.0", "--port", "8000"]
