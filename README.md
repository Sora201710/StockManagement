## Getting Started

Follow these steps to initialize the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Sora201710/StockManagement.git
cd StockManagement
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv ./venv
source venv/bin/activate
```

### 3. Install Dependencies

With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Verify the Installation

Make sure the venv is activated, then run the following command to test whether the project is working correctly:

```bash
python3 main.py
```

## VM Access

To setup access to the VM, follow steps below:

### 1. Install GCloud

Install [GCloud](https://docs.cloud.google.com/sdk/docs/install-sdk)

### 2. Authenticate GCLoud

```bash
gcloud auth login
```

Then

```bash
gcloud config set project project-ebd2979a-80d8-4242-978
```

### 3. Set aliases

Set the following aliases in .bashrc (Linux) or .zshrc (Mac)

```bash
alias gcssh='gcloud compute ssh --zone us-central1-c "postgres@instance-20261109-212649" --project project-ebd2979a-80d8-4242-978'

alias gcstatus='gcloud compute instances describe instance-20261109-212649 --zone us-central1-c --project project-ebd2979a-80d8-4242-978 --format="get(status)"'

alias gcon='gcloud compute instances start instance-20261109-212649 --zone us-central1-c --project project-ebd2979a-80d8-4242-978'

alias gcoff='gcloud compute instances stop instance-20261109-212649 --zone us-central1-c --project project-ebd2979a-80d8-4242-978'

alias gcvms='gcloud compute instances list --project project-ebd2979a-80d8-4242-978'

alias gcdb='gcloud compute ssh --zone us-central1-c "postgres@instance-20261109-212649" -- -L 5433:localhost:5432 -N'
```

Then

```bash
source ~/.bashrc
```

or use `source ~/.zshrc` if that's where you stored the aliases.

### 4. Workflow

Start the VM connection in another shell

```bash
gcon
gcdb
```

Try running the command (in a different shell from above)

```bash
python query.py
```

You should see 10 rows containing stock data.

Once done, close the VM connection and do

```bash
gcoff
```

### SSH to VM

If you ever need to, you can ssh to the VM by doing

```
gcssh
```

You can access the postgres console directly by running

```
plsql
```
