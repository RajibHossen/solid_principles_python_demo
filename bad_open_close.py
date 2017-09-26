"""
Bad example of Open Close principle of SOLID
Both the HealthInsuranceSurveyor and ClaimApprovalManager classes work fine and
the design for the insurance system appears perfect until a new requirement to process vehicle insurance claims arises.
We now need to include a new VehicleInsuranceSurveyor class, and this should not create any problems.
But, what we also need is to modify the ClaimApprovalManager class to process vehicle insurance claims.
This is how the modified ClaimApprovalManager will be:
"""


class HealthInsuranceSurveyor(object):

    def is_valid_claim(self):
        print "HealthInsuranceSurveyor: Validating health insurance claim..."
        return True

# Now new insurance verification comes, vehiclesinsurance surveyor, we can add new class
# but we need to approve this in ClaimApprovalManager class
# for that we need to modify this class


class VehicleInsuranceSurveyor(object):

    def is_valid_claim(self):
        print "VehicleInsuranceSurveyor: Validating vehicle insurance claim..."
        return True


class ClaimApprovalManager(object):

    def process_health_claim(self, health_insurance_surveyor_obj):
        if health_insurance_surveyor_obj.is_valid_claim():
            print "ClaimApprovalManager: Valid claim. Currently processing claim for approval...."

    # When we need to process new claim, we need to add here i.e. we are modifying this class which
    # violates OCP of SOLID
    def process_vehicle_claim(self, vehicle_insurance_surveyor_obj):
        if vehicle_insurance_surveyor_obj.is_valid_claim():
            print "ClaimApprovalManager: Valid claim. Currently processing claim for approval...."


# In the example above,
# we modified the ClaimApprovalManager class by adding a new processVehicleClaim()
# method to incorporate a new functionality (claim approval of vehicle insurance).

# As apparent, this is a clear violation of the Open Closed Principle.
# We need to modify the class to add support for a new functionality.
# In fact, we violated the Open Closed Principle at the very first instance we wrote the ClaimApprovalManager class.

if __name__ == '__main__':
    health_insurance = HealthInsuranceSurveyor()
    vehicle_insurance = VehicleInsuranceSurveyor()

    claim_approval = ClaimApprovalManager()
    claim_approval.process_health_claim(health_insurance)
    claim_approval.process_vehicle_claim(vehicle_insurance)