const carVariable = function () {
  const seats = 5;
  const doors = 4;
  this.accept = function (visitorObject) {
    visitorObject.visit(this);
  };
};

const truckVariable = function () {
  const towPackage = true;
  const doors = 2;
  this.accept = function (visitorObject) {
    visitorObject.visit(this);
  };
};

const monsterTruckVariable = function () {
  const looksLikeADragon = true;
  const doors = 1.5;
  this.accept = function (visitorObject) {
    visitorObject.visit(this);
  };
};

const CarVisitor = function () {
  this.visit = function (car) {
    if (car.seats > 2) {
      console.log("this is clearly a car for old people");
    } else {
      console.log("My bet is this car has at least 2 cylinders");
    }
  };
};

const TruckVisitor = function () {
  this.visit = function (truckVar) {
    if (truckVar.towPackage) {
      console.log("we need to buy a boat");
    }
  };
};

const MonsterTruckVisitor = function () {
  this.visit = function (monsterTruckVar) {
    if (monsterTruckVar.looksLikeADragon) {
      console.log("that is a badass monster truck");
    } else {
      console.log("loser");
    }
  };
};

const myCar = new carVariable();
myCar.seats = 2;
myCar.accept(new CarVisitor());

const myMonsterTruck = new monsterTruckVariable();
myMonsterTruck.looksLikeADragon = false;
myMonsterTruck.accept(new MonsterTruckVisitor());

const myCar2 = new carVariable();
myCar2.seats = 2;
myCar2.accept(new MonsterTruckVisitor());
