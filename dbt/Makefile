attach_dbt:
	docker build -t journal_dbt .
	docker run -it \
		--rm \
		--volume $$(pwd):/app \
		journal_dbt

interative_dbt:
	docker run -it --rm journal_dbt /bin/bash
