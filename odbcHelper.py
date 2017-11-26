def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters.

    Returns string."""
    #return "The connection strings are as follows:\n" + "; ".join(["%s = %s" % (k, v) for k, v in params.items()]);
    return "; ".join(["%s=%s" % (k, v) for k, v in params.items()]);


if __name__ == "__main__":
    myParams = {"server":"mpilgrim",
    "database":"master",
    "uid":"sa",
    "pwd":"secret"}
    print (buildConnectionString(myParams));
    myParams["database"] = "slave";
    #print buildConnectionString(myParams);
    myParams["pid"] = "2020";
    newParams =  buildConnectionString(myParams);
    #print newParams;
    newParamsList = newParams.split("; ");
    print (newParamsList);
    #print tuple(newParamsList);

    newDict = {}
    newDict["key1"] = "value1";
    newDict["key1"] = "value1_1"
    print ("print  new dictionary: ", newDict);
    newDict["Key1"] = "value2";
    print ("print added new item in a dictionary: ", newDict);
    del newDict["Key1"];
    print ("delete one item by key: ", newDict);

    aList = ["a","j","x","d","n"];
    print ("before sorted: ", aList);
    print ("after sorted: ", sorted(aList));
    aList.append("cool");
    print ("Append a new element", aList);
    aList.append("motherfucker");
    print ("Append a 2nd element", aList);
    print ("a list sorted after append: ", sorted(aList));

    createTuple = ("a","b","c","d","hack","my","anus","brah")
    print ("original tuple: ", createTuple);
    createTuple = createTuple + ("myAnus",)
    print ("after new element added: ", createTuple);
    print ("sorting tuple: ", sorted(createTuple));

    paramsTwo = {"server":"mpilgrim", "database":"master","uid":"sa", "pwd":"secret"}
    paramsListTwo = ["manu","barca","real","manc","avl","val", "get"]
    print ("declaring paramsTwo: ", paramsTwo.items());
    print ("declaring paramsListTwo: ", paramsListTwo);

    paramsListTwo.sort();
    print ("sorting paramsTwo: ", sorted(paramsTwo.items()));
    print ("paramsTwo after sorted and return to original position: ", paramsTwo);
    print ("paramsListTwo after sorted using sort():", paramsListTwo);

    voidList = []
    print ("dir (built-in function) - Returns all the methods of a (void) list: \n", dir(voidList));
