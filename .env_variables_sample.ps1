# This is a sample file for a powershell script
# is used to define environment variables, which are
# accessible through Python commands like os.environ['POSTGRES_DB'].
$env:POSTGRES_DB='editdojo_database'
$env:POSTGRES_USER='soundvision'
$env:POSTGRES_PASSWORD='put the Postgres password here'

$env:DJANGO_SETTINGS_MODULE='editdojo_project.settings'
$env:TWITTER_HOST='127.0.0.1'
$env:TWITTER_CONSUMER_KEY='put the consumer key for Twitter API here'
$env:TWITTER_CONSUMER_SECRET='put the consumer secret for Twitter API here'
$env:TWITTER_ACCESS_KEY='put the access key for Twitter API here'
$env:TWITTER_ACCESS_SECRET='put the access secret for Twitter API here'