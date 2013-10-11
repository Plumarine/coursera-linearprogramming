ASSI_FOLDER=assignmentParts
TEST_FOLDER=unitTests
CODE_FOLDER=code

all:
	(cd ${ASSI_FOLDER} && python ../${CODE_FOLDER}/main.py .)	
test:
	(cd ${TEST_FOLDER} && python ../${CODE_FOLDER}/main.py .)	

clean:
	(cd ${ASSI_FOLDER} && rm -rf *out)
	(cd ${CODE_FOLDER} && rm -rf *out)
	(cd ${TEST_FOLDER} && rm -rf *out)
