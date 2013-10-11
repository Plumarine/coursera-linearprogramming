ASSI_FOLDER=assignmentParts
TEST_FOLDER=unitTests
CODE_FOLDER=code

TEST_FILES=${shell (cd ${TEST_FOLDER} && ls dict* | grep -v "\.")}
ASSI_FILES=${shell (cd ${ASSI_FOLDER} && ls *.dict)}

%: ${TEST_FOLDER}/%
	(cd ${TEST_FOLDER} && python ../${CODE_FOLDER}/main.py $@)	
	
all:
	(cd ${ASSI_FOLDER} && python ../${CODE_FOLDER}/main.py ${ASSI_FILES})	
test:
	(cd ${TEST_FOLDER} && python ../${CODE_FOLDER}/main.py ${TEST_FILES})	

clean:
	pwd
	(cd ${ASSI_FOLDER} && rm -rf *out)
	(cd ${CODE_FOLDER} && rm -rf *out *.pyc)
	(cd ${TEST_FOLDER} && rm -rf *out)
