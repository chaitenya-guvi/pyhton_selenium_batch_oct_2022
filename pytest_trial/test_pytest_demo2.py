    import pytest
    """
    pytest-html
    pytest-ordering
    
    User ID :	mngr460028
    Password :	gezajUq
    
    syntax --html
    
    >py.test -s -v pytest_trial\test_pytest_demo.py --html=htmlreport_new.html
    
    
    Page object model  : 
    interview questions  : 
    1. https://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html
    2. https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/
    """


    @pytest.fixture()
    def setUP() :
        print("\nthis is a Setup method at start\n")
        yield
        print("\nThis is a teardown \n ")

    @pytest.mark.run(order=3)
    def test_methodA(setUP) :
        print("\n This is method A \n")

    @pytest.mark.run(order=2)
    def test_methodB(setUP) :
        print("\n This is method B \n")

    @pytest.mark.run(order=1)
    def test_methodC(setUP) :
        print("\n This is method C \n")
