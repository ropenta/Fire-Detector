# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserProfile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address=None, authentication_methods=None, company_name=None, display_organization_info=None, display_personal_info=None, display_profile=None, display_usage_history=None, profile_image_uri=None, title=None, usage_history=None, user_details=None, user_profile_last_modified_date=None):
        """
        UserProfile - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address': 'AddressInformationV2',
            'authentication_methods': 'list[AuthenticationMethod]',
            'company_name': 'str',
            'display_organization_info': 'str',
            'display_personal_info': 'str',
            'display_profile': 'str',
            'display_usage_history': 'str',
            'profile_image_uri': 'str',
            'title': 'str',
            'usage_history': 'UsageHistory',
            'user_details': 'UserInformation',
            'user_profile_last_modified_date': 'str'
        }

        self.attribute_map = {
            'address': 'address',
            'authentication_methods': 'authenticationMethods',
            'company_name': 'companyName',
            'display_organization_info': 'displayOrganizationInfo',
            'display_personal_info': 'displayPersonalInfo',
            'display_profile': 'displayProfile',
            'display_usage_history': 'displayUsageHistory',
            'profile_image_uri': 'profileImageUri',
            'title': 'title',
            'usage_history': 'usageHistory',
            'user_details': 'userDetails',
            'user_profile_last_modified_date': 'userProfileLastModifiedDate'
        }

        self._address = address
        self._authentication_methods = authentication_methods
        self._company_name = company_name
        self._display_organization_info = display_organization_info
        self._display_personal_info = display_personal_info
        self._display_profile = display_profile
        self._display_usage_history = display_usage_history
        self._profile_image_uri = profile_image_uri
        self._title = title
        self._usage_history = usage_history
        self._user_details = user_details
        self._user_profile_last_modified_date = user_profile_last_modified_date

    @property
    def address(self):
        """
        Gets the address of this UserProfile.

        :return: The address of this UserProfile.
        :rtype: AddressInformationV2
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this UserProfile.

        :param address: The address of this UserProfile.
        :type: AddressInformationV2
        """

        self._address = address

    @property
    def authentication_methods(self):
        """
        Gets the authentication_methods of this UserProfile.
        These properties cannot be modified in the PUT.   Indicates the authentication methods used by the user.

        :return: The authentication_methods of this UserProfile.
        :rtype: list[AuthenticationMethod]
        """
        return self._authentication_methods

    @authentication_methods.setter
    def authentication_methods(self, authentication_methods):
        """
        Sets the authentication_methods of this UserProfile.
        These properties cannot be modified in the PUT.   Indicates the authentication methods used by the user.

        :param authentication_methods: The authentication_methods of this UserProfile.
        :type: list[AuthenticationMethod]
        """

        self._authentication_methods = authentication_methods

    @property
    def company_name(self):
        """
        Gets the company_name of this UserProfile.
        The name of the user's Company.

        :return: The company_name of this UserProfile.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this UserProfile.
        The name of the user's Company.

        :param company_name: The company_name of this UserProfile.
        :type: str
        """

        self._company_name = company_name

    @property
    def display_organization_info(self):
        """
        Gets the display_organization_info of this UserProfile.
         When set to **true**, the user's company and title information are shown on the ID card. 

        :return: The display_organization_info of this UserProfile.
        :rtype: str
        """
        return self._display_organization_info

    @display_organization_info.setter
    def display_organization_info(self, display_organization_info):
        """
        Sets the display_organization_info of this UserProfile.
         When set to **true**, the user's company and title information are shown on the ID card. 

        :param display_organization_info: The display_organization_info of this UserProfile.
        :type: str
        """

        self._display_organization_info = display_organization_info

    @property
    def display_personal_info(self):
        """
        Gets the display_personal_info of this UserProfile.
        When set to **true**, the user's Address and Phone number are shown on the ID card.

        :return: The display_personal_info of this UserProfile.
        :rtype: str
        """
        return self._display_personal_info

    @display_personal_info.setter
    def display_personal_info(self, display_personal_info):
        """
        Sets the display_personal_info of this UserProfile.
        When set to **true**, the user's Address and Phone number are shown on the ID card.

        :param display_personal_info: The display_personal_info of this UserProfile.
        :type: str
        """

        self._display_personal_info = display_personal_info

    @property
    def display_profile(self):
        """
        Gets the display_profile of this UserProfile.
        When set to **true**, the user's ID card can be viewed from signed documents and envelope history.

        :return: The display_profile of this UserProfile.
        :rtype: str
        """
        return self._display_profile

    @display_profile.setter
    def display_profile(self, display_profile):
        """
        Sets the display_profile of this UserProfile.
        When set to **true**, the user's ID card can be viewed from signed documents and envelope history.

        :param display_profile: The display_profile of this UserProfile.
        :type: str
        """

        self._display_profile = display_profile

    @property
    def display_usage_history(self):
        """
        Gets the display_usage_history of this UserProfile.
        When set to **true**, the user's usage information is shown on the ID card.

        :return: The display_usage_history of this UserProfile.
        :rtype: str
        """
        return self._display_usage_history

    @display_usage_history.setter
    def display_usage_history(self, display_usage_history):
        """
        Sets the display_usage_history of this UserProfile.
        When set to **true**, the user's usage information is shown on the ID card.

        :param display_usage_history: The display_usage_history of this UserProfile.
        :type: str
        """

        self._display_usage_history = display_usage_history

    @property
    def profile_image_uri(self):
        """
        Gets the profile_image_uri of this UserProfile.
        

        :return: The profile_image_uri of this UserProfile.
        :rtype: str
        """
        return self._profile_image_uri

    @profile_image_uri.setter
    def profile_image_uri(self, profile_image_uri):
        """
        Sets the profile_image_uri of this UserProfile.
        

        :param profile_image_uri: The profile_image_uri of this UserProfile.
        :type: str
        """

        self._profile_image_uri = profile_image_uri

    @property
    def title(self):
        """
        Gets the title of this UserProfile.
        

        :return: The title of this UserProfile.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this UserProfile.
        

        :param title: The title of this UserProfile.
        :type: str
        """

        self._title = title

    @property
    def usage_history(self):
        """
        Gets the usage_history of this UserProfile.

        :return: The usage_history of this UserProfile.
        :rtype: UsageHistory
        """
        return self._usage_history

    @usage_history.setter
    def usage_history(self, usage_history):
        """
        Sets the usage_history of this UserProfile.

        :param usage_history: The usage_history of this UserProfile.
        :type: UsageHistory
        """

        self._usage_history = usage_history

    @property
    def user_details(self):
        """
        Gets the user_details of this UserProfile.

        :return: The user_details of this UserProfile.
        :rtype: UserInformation
        """
        return self._user_details

    @user_details.setter
    def user_details(self, user_details):
        """
        Sets the user_details of this UserProfile.

        :param user_details: The user_details of this UserProfile.
        :type: UserInformation
        """

        self._user_details = user_details

    @property
    def user_profile_last_modified_date(self):
        """
        Gets the user_profile_last_modified_date of this UserProfile.
        

        :return: The user_profile_last_modified_date of this UserProfile.
        :rtype: str
        """
        return self._user_profile_last_modified_date

    @user_profile_last_modified_date.setter
    def user_profile_last_modified_date(self, user_profile_last_modified_date):
        """
        Sets the user_profile_last_modified_date of this UserProfile.
        

        :param user_profile_last_modified_date: The user_profile_last_modified_date of this UserProfile.
        :type: str
        """

        self._user_profile_last_modified_date = user_profile_last_modified_date

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other