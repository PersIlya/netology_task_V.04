
import sentry_sdk

sentry_sdk.init(
    dsn="https://4014e1ea7cca11c15b0b7133ac0216b2@o4508710562103296.ingest.us.sentry.io/4508710653460480",
    environment="development",
    release="1.0"
)
if  __name__ == "__main__":
	division_by_zero = 1 / 0
