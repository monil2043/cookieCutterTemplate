# Notes for a developer using this code

# start docker
# setup sso like mentioned in sso.md
aws sso login --profile dev
yawsso -p dev
export AWS_PROFILE=dev

# to generate a new project from template
cookiecutter /Users/jyoti.rathi/ContactCenterOnAWS/backend-integrations-template


cd demo_service_rest_backend
make dev
make lint
make complex
make deploy


# we will need this later when pushing a new repo to ORG
git init
git remote add origin git@github.com:ContactCenterOnAWS/demo-service-rest-backend
curl -L -X POST -H "Accept: application/vnd.github+json" -H "Authorization: Bearer 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" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/orgs/ContactCenterOnAWS/repos -d '{"name":"demo-service-rest-backend","description":"This is your first repository","homepage":"https://github.com","private":true,"has_issues":true,"has_projects":false,"has_wiki":true}'
git checkout -b main
git add .
git commit -m "Autogenerated Code"
git push -u origin main




# to update package-lock.json
Delete the currently checked in package-lock.json file from the template repository
Change dev target in Make file to say "npm install" instead of "npm ci"
Generate a new dummy project from the template
Copy the generated package-lock.json file from the generated project folder into the template project folde
Finally, change back "npm install" in dev target in Makefile to "npm ci"



export $(grep -v '^#' .env | xargs)