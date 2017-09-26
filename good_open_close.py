"""
Good example of OCP of SOLID
"""

from abc import ABCMeta, abstractmethod

class InsuranceSurveyor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_valid_claim(self):
        pass

class HealthInsuranceSurveyor(InsuranceSurveyor):
    def is_valid_claim(self):
        print "HealthInsuranceSurveyor: Validating health insurance claim..."
        return True


class VehicleInsuranceSurveyor(InsuranceSurveyor):
    def is_valid_claim(self):
        print "VehicleInsuranceSurveyor: Validating vehicle insurance claim..."
        return True


class HomeInsuranceSurveyor(InsuranceSurveyor):
    def is_valid_claim(self):
        print "HomeInsuranceSurveyor: Validating home insurance claim..."
        return True


class ClaimApprovalManager(object):

    def process_claim(self, insurance_surveyor):
        if insurance_surveyor.is_valid_claim():
            print "ClaimApprovalManager: Valid claim. Currently processing claim for approval...."


if __name__ == '__main__':
    health_insurance = HealthInsuranceSurveyor()
    vehicle_insurance = VehicleInsuranceSurveyor()
    home_insurance = HomeInsuranceSurveyor()

    claim_approval_manager = ClaimApprovalManager()
    claim_approval_manager.process_claim(health_insurance)
    claim_approval_manager.process_claim(vehicle_insurance)
    claim_approval_manager.process_claim(home_insurance)