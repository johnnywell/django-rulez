#-*- coding: utf-8 -*-

class AbstractRole(object):
    """
    This is an abstract class to show what a role should look like
    """

    # This is the list of rules in this role, used to easy execution and validation of rules
    # Each rule declared in this role must be in the rules list to execute.
    rules = ['is_member']

    @classmethod
    def is_member(cls, user, obj): #pragma: nocover
        raise NotImplemented

    @classmethod
    def evaluate_rules(cls, user, obj):
        """
        Avaluate all rules of the role for an user.
        """
        rules_number = len(cls.rules)
        valid_rules = 0
        for rule in cls.rules:
            rule = getattr(cls, rule)
            if callable(rule):
                if rule(user, obj):
                    valid_rules += 1
        return rules_number == valid_rules