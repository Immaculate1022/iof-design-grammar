import React from 'react';

interface TrustMarkersProps {
  creatorName: string;
  creatorLocation: string;
  purposeStatement: string;
  licenseNote: string;
  privacyNote: string;
  versionHash?: string;
  githubLink?: string;
}

const TrustMarkers: React.FC<TrustMarkersProps> = ({
  creatorName,
  creatorLocation,
  purposeStatement,
  licenseNote,
  privacyNote,
  versionHash,
  githubLink,
}) => {
  return (
    <div className="iof-trust-markers text-xs text-gray-500 p-4 border-t border-gray-700 mt-8">
      <p>
        {purposeStatement} by {creatorName}, {creatorLocation}.
      </p>
      <p>{licenseNote}</p>
      <p>{privacyNote}</p>
      {versionHash && <p>Version: {versionHash}</p>}
      {githubLink && (
        <p>
          Source: <a href={githubLink} target="_blank" rel="noopener noreferrer" className="text-blue-400 hover:underline">GitHub</a>
        </p>
      )}
      <p className="mt-2">Optimized for Human and Machine implementation.</p>
    </div>
  );
};

export default TrustMarkers;
