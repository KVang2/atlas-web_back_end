export default function createReportObject(employeesList) {
  const allEmployees = {};
  for (const department in employeesList) {
    if (Object.hasOwn(employeesList, department)) {
      allEmployees[department] = employeesList[department];
    }
  }
  const getNumberOfDepartments = () => Object.keys(allEmployees).length;
  return { allEmployees, getNumberOfDepartments };
}
