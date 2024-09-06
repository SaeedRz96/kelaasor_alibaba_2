from celery import shared_task


@shared_task(bind=True, default_retry_delay= 5)
def send_email_to_customer(self,customer_email):
    try:
        pass
    except Exception as e:
        return self.retry(exc=e,max_retries=10)