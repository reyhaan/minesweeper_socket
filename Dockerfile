FROM python:3.6

COPY . /shuttle-tracking
WORKDIR /shuttle-tracking

RUN python -m pip install --upgrade pip && \
  pip install --upgrade setuptools && \
  pip install -r requirements.txt

CMD python app.py

EXPOSE 3000